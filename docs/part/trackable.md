---
title: Trackable Parts
---

Denoting a part as *Trackble* changes the way that [stock items](../../stock/stock) associated with the particular part are handled in the database. A trackable part also has more restrictions imposed by the database scheme.

## Stock Tracking

For many parts in an InvenTree database, simply tracking current stock levels (and locations) is sufficient. However, some parts require more extensive tracking than simple stock level knowledge.

Any stock item associated with a trackable part *must* have either a batch number or a serial number. This includes stock created manually or via an internal process (such as a [Purchase Order](../../buy/po) or a [Build Order](/../../build/build)).




## Build Orders

Build orders have some extra requirements when either building a trackable part, or using parts in the Bill of Materials which are themselves trackable.