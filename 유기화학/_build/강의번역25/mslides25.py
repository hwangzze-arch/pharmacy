# -*- coding: utf-8 -*-
"""25장 슬라이드 옆 그림: 반응식(fig.row)."""
from fig import row as RX

MS = {}
FIRST_ROWS = {}
ANS_FULL = {}

GLC = 'OC[C@H]1O[C@H](O)[C@H](O)[C@@H](O)[C@@H]1O'      # β-D-글루코피라노스
AGLC = 'OC[C@H]1O[C@@H](O)[C@H](O)[C@@H](O)[C@@H]1O'    # α
OPEN = 'O=C[C@H](O)[C@@H](O)[C@H](O)[C@H](O)CO'          # D-포도당 열린 사슬

MS[16] = [RX(('m', 'CC=O', 45, 35), ('t', '+'), ('m', 'CO', 35, 30), ('a', 'H⁺', '⇌'), ('m', 'CC(O)OC', 60, 45), ('t', '헤미아세탈'), ('t', ' · 당:'), ('m', OPEN, 120, 60), ('a', 'C5–OH → C1', '고리화'), ('m', GLC, 90, 70))]
MS[22] = [RX(('m', GLC, 90, 70), ('a', 'CH₃OH, HCl', '−H₂O'), ('m', 'OC[C@H]1O[C@H](OC)[C@H](O)[C@@H](O)[C@@H]1O', 95, 70), ('t', 'β 33 %'), ('m', 'OC[C@H]1O[C@@H](OC)[C@H](O)[C@@H](O)[C@@H]1O', 95, 70), ('t', 'α 66 %'))]
MS[26] = [RX(('m', GLC, 85, 65), ('a', '⇌', '열린 사슬'), ('m', OPEN, 120, 55), ('a', 'NaBH₄', 'H₂O'), ('m', 'OC[C@H](O)[C@@H](O)[C@H](O)[C@H](O)CO', 120, 55), ('t', 'D-글루시톨 (소르비톨)'))]
MS[27] = [RX(('m', OPEN, 110, 50), ('a', 'Br₂, H₂O', 'C1만'), ('m', 'O=C(O)[C@H](O)[C@@H](O)[C@H](O)[C@H](O)CO', 120, 50), ('t', '알돈산'))
          + RX(('m', OPEN, 110, 50), ('a', 'HNO₃, Δ', 'C1 + C6'), ('m', 'O=C(O)[C@H](O)[C@@H](O)[C@H](O)[C@H](O)C(=O)O', 130, 50), ('t', '알다르산'))]
MS[31] = [RX(('m', 'O=C[C@H](O)CO', 60, 40), ('a', 'HCN', ''), ('m', 'N#CC(O)[C@H](O)CO', 75, 45), ('a', '1. H₂, Pd', '2. H₃O⁺'), ('m', 'O=CC(O)[C@H](O)CO', 70, 45), ('t', 'C2 에피머 두 개 (+1 C)'))]
MS[32] = [RX(('m', 'O=C[C@H](O)[C@@H](O)CO', 70, 45), ('a', 'NH₂OH', ''), ('m', 'ON=C[C@H](O)[C@@H](O)CO', 85, 45), ('a', 'Ac₂O', '−H₂O'), ('m', 'N#C[C@H](O)[C@@H](O)CO', 80, 45), ('a', 'NaOCH₃', '−HCN'), ('m', 'O=C[C@@H](O)CO', 55, 40), ('t', '(−1 C)'))]
