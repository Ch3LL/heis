# Import python libs
import re
from typing import Dict


def check(hub, tgt: str, condition: Dict[str:...]) -> bool:
    '''
    Check that the `id` in the condition glob matches the passed tgt
    '''
    if 'id' not in condition:
        return False
    return bool(re.match(tgt, condition['id']))

