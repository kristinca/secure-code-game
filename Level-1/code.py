'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  ///
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stucked then read the hint                   ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')


MAX_ITEM_AMOUNT = 100000 # maximum price of item in the shop
MIN_ITEM_AMOUNT = 1 # minimum price of item in the shop
MAX_QUANTITY = 100 # maximum quantity of an item in the shop
MIN_QUANTITY = 1 # minimum quantity of an item in the shop
MAX_TOTAL = 1e6 # maximum total amount accepted for an order

def validorder(order: Order):
    net = 0

    for item in range(len(order.items)):
        if order.items[item].type == 'payment' and MIN_ITEM_AMOUNT < order.items[item].amount < MAX_ITEM_AMOUNT:
            net += order.items[item].amount
        elif order.items[item].type == 'product':
            if order.items[item].quantity < MAX_QUANTITY and MIN_ITEM_AMOUNT <= order.items[item].amount < MAX_ITEM_AMOUNT:
                net -= order.items[item].amount * order.items[item].quantity
            if -MAX_TOTAL > float(net) > MAX_TOTAL:
                return "Total amount exceeded"
        elif order.items[item].type not in ('product', 'payment'):
            return f"Invalid item type: {order.items[item].type}"

        if net != 0:
            return f"Order ID: {order.id} - Payment imbalance: ${net:.2f}"
        elif net > 0:
            return f"Order ID: {order.id} - Full payment received!"
