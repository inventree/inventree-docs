---
title: Pricing
---

## Pricing

InvenTree provides multi-currency pricing support via the [django-money](https://django-money.readthedocs.io/en/latest/) library.

Cost - The theoretical amount of money required to pay for something.  
Price - The actual amount of money paid.  


| Price | Description | Linked to |
| --- | --- | ---| 
| Supplier Cost | How much it costs to theoretically purchase a part from a given supplier | Supplier |
| Purchase Price | Historical pricing information for parts actually purchased | Stock Item |
| Internal Cost | How much a part costs to make | Part |
| BOM Cost | Total cost for an assembly (total cost of component items) | Part |
| Sale Cost | How much a salable item is sold for (with cost-breaks) | Part |
| Sale Price | How much an item was actually sold for | Sales Order |

## Pricing Tab

The pricing tab of a part provides all avalable pricing information for that part. It shows all price ranges and provides tools to calculate them.

### Price ranges
As parts can have price ranges it is important to set the correct amount in the first panel to get an accurate price.

### Currency in the graphs and tables
All money-values are adjusted to the default currency at the current exchange rates (see [currency conversion](#Currency Conversion) for more information). This can squew historical data but is necessary to easaly compare values.

### Supplier cost / prices

Shows how much it would cost to purchase the part right now from a supplier/manufacturer (can have [price ranges](#price-ranges)).  
Also provides a graph of historical prices collected from stock in the tab **Purchase Price**.

### Internal cost / prices

Parts can optionally have a internal cost (this needs to be enabled by a admin) that is used for internal sales. This value is used for BOM calculations (if the part is an assambly the internal cost has to contain the cost for all sub-parts). [Price ranges](#price-ranges) are supported.

### BOM cost

If a part is an assembly this panel will show the cost (possibly as range) for all sub-parts and a graph how much each part contirbutes to the total cost.

### Sale cost / prices

Sale prices are always to customers (through [sale orders](../companies/so.md)) and support [price ranges](#price-ranges).

The panel also shows historical sale price information collected from past [purchase orders](../companies/po.md).

## Considerations for pricing

Pricing in InvenTree supports various degrees of complexity. The following use cases provide an insight into possible ways to use the available tools.

TODO

## Currency conversion

Automatic updating of currency conversion rates can be provided via the [exchangerate.host](https://exchangerate.host/#/) API.

Currency exchange rates are updated once per day.

The rates can also be set manually in the settings. Be aware that most companies trade with hourly or daily rates – setting a static rate can lead to big differences to the real world.
