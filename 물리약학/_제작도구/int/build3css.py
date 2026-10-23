import os
from lib import HERE
CSS = open(os.path.join(HERE, 'style4.css'), encoding='utf-8').read() + '''
body { font-size: 13px; line-height: 1.52; }
.page { padding: 8mm 11mm 0; display: flex; flex-direction: column; }
.ptop { margin-bottom: 8px; padding-bottom: 5px; border-bottom-width: 1.5px; }
.ptop .pl { font-size: 11px; padding: 2px 9px; } .ptop .pt { font-size: 14px; } .ptop .pr { font-size: 11px; }
.pbox { display: flex; flex-direction: column; gap: 9px; height: 676px; }
.prow { flex: 1 1 auto; display: grid; grid-template-columns: 0.9fr 1.1fr; gap: 10px; margin: 0 !important; padding: 0 !important; border: 0 !important; }
.pq { display: flex; flex-direction: column; }
.qcard { border: 1px solid #d6dbe4; border-radius: 9px; padding: 7px 11px; background: #fff; }
.qh { margin-bottom: 4px; gap: 6px; } .qh .n { font-size: 11.5px; padding: 0 8px; border-radius: 5px; }
.qh .s { font-size: 10px; padding: 0 7px; border-width: 1px; } .qh .t { font-size: 13.4px; }
.qq { font-size: 13.2px; margin-bottom: 3px; } .chs { font-size: 12.8px; gap: 0 12px; }
.mine { flex: 1 1 auto; min-height: 34px; height: auto; margin-top: 6px; border: 1.2px dashed #cfd5df; border-radius: 9px; background-size: 13px 13px; }
.mine span { font-size: 10.5px; top: 4px; left: 8px; padding: 0 6px; }
.sol { border: 1px solid #cfe5d6; background: #f6faf7; border-radius: 9px; padding: 7px 11px; display: flex; flex-direction: column; }
.sol .ans { font-size: 14px; margin-bottom: 2px; } .sol .ans .lb { font-size: 10px; }
.sol .sh { font-size: 12px; margin: 3px 0 2px; }
.sol .brain { margin-top: auto; font-size: 12.2px; padding: 5px 10px; }
.fl { padding-bottom: 2px; gap: 7px; } .fl .ic { width: 21px; height: 21px; font-size: 11px; }
.fl:not(:last-child)::before { left: 10px; top: 21px; }
.fl .tx { font-size: 12.6px; padding-top: 1px; } .fl .tg { font-size: 10px; }
.warn, .fixnote, .mynote { font-size: 12px; padding: 4px 10px; margin: 3px 0; }
table { font-size: 12px; } .img img { max-height: 95px !important; }
.cs { grid-template-columns: repeat(4, 1fr); gap: 7px; }
.cs > div { padding: 6px 10px; border-width: 1px; }
.cs .f { font-size: 13.2px; line-height: 1.38; } .cs .d { font-size: 11.6px; line-height: 1.4; } .cs .h { font-size: 11px; }
.brain { font-size: 12.8px; padding: 6px 11px; }
.title { display: flex; align-items: baseline; gap: 12px; border-bottom: 2.5px solid #1d6db1; padding-bottom: 5px; margin-bottom: 8px; }
.title h1 { margin: 0; font-size: 21px; } .title span { color: #555; font-size: 12.5px; }
.legend { font-size: 12px; color: #444; margin: 0 0 7px; }
.foot { bottom: 4.5mm; font-size: 9.5px; left: 11mm; right: 11mm; }
'''
