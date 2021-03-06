
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightUSEPARATORLETTER NUMBER SEPARATORexpressions : NUMBER expressionexpression : LETTER NUMBERexpressions : expressions SEPARATOR expressions %prec USEPARATOR'
    
_lr_action_items = {'NUMBER':([0,3,5,],[2,2,7,]),'$end':([1,4,6,7,],[0,-1,-3,-2,]),'SEPARATOR':([1,4,6,7,],[3,-1,-3,-2,]),'LETTER':([2,],[5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expressions':([0,3,],[1,6,]),'expression':([2,],[4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expressions","S'",1,None,None,None),
  ('expressions -> NUMBER expression','expressions',2,'p_expression_long','SimpleParser.py',44),
  ('expression -> LETTER NUMBER','expression',2,'p_expression_shout','SimpleParser.py',48),
  ('expressions -> expressions SEPARATOR expressions','expressions',3,'p_expression_long_separator_long','SimpleParser.py',52),
]
