from typing import Callable, List
"""
>>> makeTwoBitStrOneLiner(2)
... ['00', '01', '10', '11']
"""

makeTwoBitStrOneLiner: Callable[[int, List[str]], List[str]] = lambda num, bits=['']: (lambda bits: [*['0'+item for item in bits], *['1'+item for item in bits]])(makeTwoBitStrOneLiner(num-1, bits)) if num > 0 else bits
