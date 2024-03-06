# 用于识别NAT类型和控制内网穿透行为的命令模块

import json

# NAT类型
NAT_F_TO_F      = 0x1       # Full Cone to Full Cone
NAT_F_TO_R      = 0x2       # ...
NAT_F_TO_RP     = 0x3       # ... 
NAT_F_TO_S      = 0x4       # ...
NAT_R_TO_R      = 0x5       # ...
NAT_R_TO_RP     = 0x6       # ...
NAT_R_TO_S      = 0x7       # ...
NAT_RP_TO_RP    = 0x8       # ...
NAT_RP_TO_S     = 0x9       # ...
NAT_RP_TO_S     = 0xa       # ...

"""
different commands payloads

"""

class Commands:
    self

    
