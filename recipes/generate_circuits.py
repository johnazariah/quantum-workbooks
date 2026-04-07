"""Generate clean textbook-style circuit diagram PNGs."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

RECIPES = os.path.dirname(os.path.abspath(__file__))
DPI = 200


class CircuitDrawer:
    """Minimal textbook-style quantum circuit renderer."""

    def __init__(self, n_qubits, n_cols, figscale=0.6):
        self.n = n_qubits
        self.cols = n_cols
        self.col_w = 1.0
        self.row_h = 0.8
        self.gate_w = 0.5
        self.gate_h = 0.5
        self.figscale = figscale

        w = (n_cols + 2) * self.col_w
        h = (n_qubits + 0.5) * self.row_h
        self.fig, self.ax = plt.subplots(figsize=(w * figscale, h * figscale))
        self.ax.set_xlim(-0.5, (n_cols + 1) * self.col_w)
        self.ax.set_ylim(-0.3, n_qubits * self.row_h + 0.1)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        self.fig.patch.set_facecolor('white')

        for i in range(n_qubits):
            y = self._y(i)
            self.ax.plot([-0.2, (n_cols + 0.5) * self.col_w], [y, y],
                        color='#333333', linewidth=1.0, zorder=0)
            self.ax.text(-0.45, y, f'q[{i}]',
                        ha='right', va='center', fontsize=9, fontfamily='monospace',
                        color='#333333')

    def _y(self, qubit):
        return (self.n - 1 - qubit) * self.row_h

    def _x(self, col):
        return (col + 0.8) * self.col_w

    def gate(self, qubit, col, label, color='#4A90D9', textcolor='white'):
        x, y = self._x(col), self._y(qubit)
        rect = patches.FancyBboxPatch(
            (x - self.gate_w/2, y - self.gate_h/2), self.gate_w, self.gate_h,
            boxstyle='round,pad=0.05', facecolor=color, edgecolor='#333333',
            linewidth=1.0, zorder=2)
        self.ax.add_patch(rect)
        self.ax.text(x, y, label, ha='center', va='center',
                    fontsize=10, fontweight='bold', color=textcolor, zorder=3)

    def gate2(self, qubit, col, label, color='#4A90D9', textcolor='white'):
        x, y = self._x(col), self._y(qubit)
        w = self.gate_w * 1.4
        rect = patches.FancyBboxPatch(
            (x - w/2, y - self.gate_h/2), w, self.gate_h,
            boxstyle='round,pad=0.05', facecolor=color, edgecolor='#333333',
            linewidth=1.0, zorder=2)
        self.ax.add_patch(rect)
        self.ax.text(x, y, label, ha='center', va='center',
                    fontsize=8, fontweight='bold', color=textcolor, zorder=3)

    def ctrl(self, qubit, col):
        x, y = self._x(col), self._y(qubit)
        self.ax.plot(x, y, 'o', color='#333333', markersize=6, zorder=3)

    def targ(self, qubit, col):
        x, y = self._x(col), self._y(qubit)
        circle = plt.Circle((x, y), 0.15, fill=False, edgecolor='#333333',
                            linewidth=1.5, zorder=3)
        self.ax.add_patch(circle)
        self.ax.plot([x-0.15, x+0.15], [y, y], color='#333333', linewidth=1.5, zorder=3)
        self.ax.plot([x, x], [y-0.15, y+0.15], color='#333333', linewidth=1.5, zorder=3)

    def cnot(self, ctrl_q, targ_q, col):
        self.ctrl(ctrl_q, col)
        self.targ(targ_q, col)
        x = self._x(col)
        y1, y2 = self._y(ctrl_q), self._y(targ_q)
        self.ax.plot([x, x], [min(y1,y2), max(y1,y2)],
                    color='#333333', linewidth=1.0, zorder=1)

    def ccx(self, c1, c2, targ, col):
        self.ctrl(c1, col)
        self.ctrl(c2, col)
        self.targ(targ, col)
        x = self._x(col)
        ys = [self._y(q) for q in [c1, c2, targ]]
        self.ax.plot([x, x], [min(ys), max(ys)],
                    color='#333333', linewidth=1.0, zorder=1)

    def cp(self, c, t, col, label='P'):
        self.ctrl(c, col)
        self.gate(t, col, label, color='#7B68EE', textcolor='white')
        x = self._x(col)
        y1, y2 = self._y(c), self._y(t)
        self.ax.plot([x, x], [min(y1,y2), max(y1,y2)],
                    color='#333333', linewidth=1.0, zorder=1)

    def swap(self, q1, q2, col):
        x = self._x(col)
        for q in [q1, q2]:
            y = self._y(q)
            d = 0.1
            self.ax.plot([x-d,x+d],[y-d,y+d], color='#333333', linewidth=1.5, zorder=3)
            self.ax.plot([x-d,x+d],[y+d,y-d], color='#333333', linewidth=1.5, zorder=3)
        y1, y2 = self._y(q1), self._y(q2)
        self.ax.plot([x, x], [min(y1,y2), max(y1,y2)],
                    color='#333333', linewidth=1.0, zorder=1)

    def measure(self, qubit, col):
        x, y = self._x(col), self._y(qubit)
        rect = patches.FancyBboxPatch(
            (x-self.gate_w/2, y-self.gate_h/2), self.gate_w, self.gate_h,
            boxstyle='round,pad=0.05', facecolor='#F5F5F5', edgecolor='#333333',
            linewidth=1.0, zorder=2)
        self.ax.add_patch(rect)
        # "M" label — simple and unambiguous
        self.ax.text(x, y, 'M', ha='center', va='center',
                    fontsize=10, fontweight='bold', color='#333333', zorder=3)

    def barrier(self, col, qubits=None, label=None):
        if qubits is None:
            qubits = list(range(self.n))
        x = self._x(col)
        ys = [self._y(q) for q in qubits]
        self.ax.plot([x, x], [min(ys)-0.3, max(ys)+0.3],
                    color='#999999', linewidth=0.8, linestyle='--', zorder=1)
        if label:
            self.ax.text(x, max(ys)+0.38, label, ha='center', va='bottom',
                        fontsize=7, color='#666666', fontstyle='italic')

    def save(self, name, subdir):
        path = os.path.join(RECIPES, subdir, name)
        self.fig.savefig(path, dpi=DPI, bbox_inches='tight', facecolor='white', pad_inches=0.15)
        plt.close(self.fig)
        print(f'  saved {path}')


# ── Recipe 01 ──
print('Recipe 01: Bell State')
d = CircuitDrawer(2, 4)
d.gate(0, 0, 'H')
d.cnot(0, 1, 1)
d.measure(0, 2)
d.measure(1, 3)
d.save('circuit.png', '01-bell-state')

# ── Recipe 02 ──
print('Recipe 02: Teleportation')
d = CircuitDrawer(3, 10)
d.gate(0, 0, 'X', color='#D94A4A')
d.barrier(0.7)
d.gate(1, 1, 'H')
d.cnot(1, 2, 2)
d.barrier(2.7)
d.cnot(0, 1, 3)
d.gate(0, 4, 'H')
d.measure(0, 5)
d.measure(1, 6)
d.barrier(6.7)
d.gate(2, 7, 'X', color='#D94A4A')
d.gate(2, 8, 'Z', color='#4CAF50')
d.measure(2, 9)
d.ax.annotate('', xy=(d._x(7), d._y(2)-0.25), xytext=(d._x(6), d._y(1)-0.25),
             arrowprops=dict(arrowstyle='->', color='#999999', lw=0.8, ls='--'))
d.ax.annotate('', xy=(d._x(8), d._y(2)-0.25), xytext=(d._x(5), d._y(0)-0.25),
             arrowprops=dict(arrowstyle='->', color='#999999', lw=0.8, ls='--'))
d.save('circuit.png', '02-teleportation')

# ── Recipe 03 (balanced) ──
print('Recipe 03: Deutsch-Jozsa (balanced)')
d = CircuitDrawer(3, 7)
d.gate(2, 0, 'X', color='#D94A4A')
d.gate(0, 1, 'H'); d.gate(1, 1, 'H'); d.gate(2, 1, 'H')
d.barrier(1.7, label='Oracle')
d.cnot(0, 2, 2)
d.cnot(1, 2, 3)
d.barrier(3.7)
d.gate(0, 4, 'H'); d.gate(1, 4, 'H')
d.measure(0, 5); d.measure(1, 6)
d.save('circuit_balanced.png', '03-deutsch-jozsa')

# ── Recipe 03 (constant) ──
print('Recipe 03: Deutsch-Jozsa (constant)')
d = CircuitDrawer(3, 6)
d.gate(2, 0, 'X', color='#D94A4A')
d.gate(0, 1, 'H'); d.gate(1, 1, 'H'); d.gate(2, 1, 'H')
d.barrier(1.7, label='Oracle (I)')
d.barrier(2.3)
d.gate(0, 3, 'H'); d.gate(1, 3, 'H')
d.measure(0, 4); d.measure(1, 5)
d.save('circuit_constant.png', '03-deutsch-jozsa')

# ── Recipe 04 ──
print('Recipe 04: Bernstein-Vazirani')
d = CircuitDrawer(4, 8)
d.gate(3, 0, 'X', color='#D94A4A')
d.gate(0, 1, 'H'); d.gate(1, 1, 'H'); d.gate(2, 1, 'H'); d.gate(3, 1, 'H')
d.barrier(1.7, label='Oracle: s=101')
d.cnot(0, 3, 2); d.cnot(2, 3, 3)
d.barrier(3.7)
d.gate(0, 4, 'H'); d.gate(1, 4, 'H'); d.gate(2, 4, 'H')
d.measure(0, 5); d.measure(1, 6); d.measure(2, 7)
d.save('circuit.png', '04-bernstein-vazirani')

# ── Recipe 05 ──
print("Recipe 05: Simon's Problem")
d = CircuitDrawer(4, 9)
d.gate(0, 0, 'H'); d.gate(1, 0, 'H')
d.barrier(0.7, label='Oracle: s=11')
d.cnot(0, 2, 1); d.cnot(1, 3, 2); d.cnot(0, 2, 3); d.cnot(0, 3, 4)
d.barrier(4.7)
d.gate(0, 5, 'H'); d.gate(1, 5, 'H')
d.measure(0, 7); d.measure(1, 8)
d.save('circuit.png', '05-simons-problem')

# ── Recipe 06 ──
print("Recipe 06: Grover's Search")
d = CircuitDrawer(3, 15, figscale=0.5)
d.gate(0, 0, 'H'); d.gate(1, 0, 'H'); d.gate(2, 0, 'H')
for offset in [0, 7]:
    b = 1 + offset
    d.barrier(b-0.3, label='Oracle')
    d.gate(1, b, 'X', color='#D94A4A')
    d.ccx(0, 1, 2, b+1)
    d.gate(1, b+2, 'X', color='#D94A4A')
    d.barrier(b+2.7, label='Diffusion')
    d.gate(0, b+3, 'H'); d.gate(1, b+3, 'H'); d.gate(2, b+3, 'H')
    d.gate(0, b+4, 'X', color='#D94A4A'); d.gate(1, b+4, 'X', color='#D94A4A'); d.gate(2, b+4, 'X', color='#D94A4A')
    d.ccx(0, 1, 2, b+5)
d.measure(0, 14); d.measure(1, 14); d.measure(2, 14)
d.save('circuit.png', '06-grovers-search')

# ── Recipe 07 ──
print('Recipe 07: QAOA for MaxCut')
d = CircuitDrawer(3, 12, figscale=0.5)
d.gate(0, 0, 'H'); d.gate(1, 0, 'H'); d.gate(2, 0, 'H')
d.barrier(0.7, label='Problem U(γ)')
d.cnot(0, 1, 1); d.gate2(1, 2, 'Rz', color='#7B68EE'); d.cnot(0, 1, 3)
d.cnot(1, 2, 4); d.gate2(2, 5, 'Rz', color='#7B68EE'); d.cnot(1, 2, 6)
d.cnot(0, 2, 7); d.gate2(2, 8, 'Rz', color='#7B68EE'); d.cnot(0, 2, 9)
d.barrier(9.7, label='Mixer U(β)')
d.gate2(0, 10, 'Rx', color='#E67E22'); d.gate2(1, 10, 'Rx', color='#E67E22'); d.gate2(2, 10, 'Rx', color='#E67E22')
d.measure(0, 11); d.measure(1, 11); d.measure(2, 11)
d.save('circuit.png', '07-qaoa-maxcut')

# ── Recipe 08 ──
print('Recipe 08: VQE for H₂')
d = CircuitDrawer(2, 7)
d.gate(0, 0, 'X', color='#D94A4A')
d.barrier(0.7, label='Ansatz')
d.gate2(1, 1, 'Ry', color='#E67E22')
d.cnot(1, 0, 2)
d.gate2(1, 3, '-Ry', color='#E67E22')
d.cnot(1, 0, 4)
d.barrier(4.7)
d.measure(0, 5); d.measure(1, 6)
d.save('circuit.png', '08-vqe-h2')

# ── Recipe 09 ──
print('Recipe 09: QFT')
d = CircuitDrawer(3, 10)
d.gate(0, 0, 'X', color='#D94A4A'); d.gate(2, 0, 'X', color='#D94A4A')
d.barrier(0.7, label='QFT')
d.gate(0, 1, 'H')
d.cp(1, 0, 2, 'S'); d.cp(2, 0, 3, 'T')
d.gate(1, 4, 'H')
d.cp(2, 1, 5, 'S')
d.gate(2, 6, 'H')
d.swap(0, 2, 7)
d.barrier(7.7)
d.measure(0, 8); d.measure(1, 8); d.measure(2, 9)
d.save('circuit.png', '09-quantum-fourier-transform')

# ── Recipe 10 ──
print('Recipe 10: QPE')
d = CircuitDrawer(4, 13, figscale=0.5)
d.gate(3, 0, 'X', color='#D94A4A')
d.gate(0, 1, 'H'); d.gate(1, 1, 'H'); d.gate(2, 1, 'H')
d.barrier(1.7, label='Ctrl-U^2^k')
d.cp(2, 3, 2, 'T'); d.cp(1, 3, 3, 'S'); d.cp(0, 3, 4, 'Z')
d.barrier(4.7, label='QFT⁻¹')
d.swap(0, 2, 5)
d.gate(0, 6, 'H')
d.cp(1, 0, 7, '-S')
d.gate(1, 8, 'H')
d.cp(2, 0, 9, '-T')
d.cp(2, 1, 10, '-S')
d.gate(2, 11, 'H')
d.measure(0, 12); d.measure(1, 12); d.measure(2, 12)
d.save('circuit.png', '10-quantum-phase-estimation')

# ── Recipe 11 ──
print('Recipe 11: ZNE')
d = CircuitDrawer(2, 8)
d.gate(0, 0, 'H')
d.barrier(0.7, label='Noise amplification (λ=3)')
d.cnot(0, 1, 1); d.cnot(0, 1, 2); d.cnot(0, 1, 3); d.cnot(0, 1, 4)
d.barrier(4.7)
d.gate(0, 5, 'H')
d.measure(0, 6)
d.save('circuit.png', '11-error-mitigation-zne')

# ── Recipe 12 ──
print('Recipe 12: Quantum Counting')
d = CircuitDrawer(4, 11, figscale=0.5)
d.gate(0, 0, 'H'); d.gate(1, 0, 'H'); d.gate(2, 0, 'H'); d.gate(3, 0, 'H')
d.barrier(0.7, label='Ctrl-G¹')
d.gate2(2, 1.5, 'G', color='#E67E22'); d.gate2(3, 1.5, 'G', color='#E67E22')
x1 = d._x(1.5)
d.ax.plot([x1, x1], [d._y(1), d._y(2)], color='#333333', linewidth=1.0, zorder=1)
d.ctrl(1, 1.5)
d.barrier(2.3, label='Ctrl-G²')
d.gate2(2, 3, 'G²', color='#E67E22'); d.gate2(3, 3, 'G²', color='#E67E22')
x2 = d._x(3)
d.ax.plot([x2, x2], [d._y(0), d._y(2)], color='#333333', linewidth=1.0, zorder=1)
d.ctrl(0, 3)
d.barrier(3.7, label='QFT⁻¹')
d.swap(0, 1, 4.5)
d.gate(0, 5.5, 'H')
d.cp(1, 0, 6.5, '-S')
d.gate(1, 7.5, 'H')
d.barrier(8.3)
d.measure(0, 9); d.measure(1, 10)
d.save('circuit.png', '12-quantum-counting')

print('\nDone!')
