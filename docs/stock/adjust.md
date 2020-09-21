---
title: Stock Adjustments
layout: page
---

## Stock Adjustments

InvenTree provides simple yet powerful management of stock levels. Multiple stock adjustment options are available, and each type of adjustment is automatically tracked to maintain a complete stock history.

### Move Stock

Multiple stock items can be moved to a new location in a single operation. Each item is moved to the selected location, and a stock tracking entry is added to the stock item history.

{% with id="stock_move", url="stock/stock_move.png", description="Stock movement" %}
{% include 'img.html' %}
{% endwith %}

### Add Stock

Add parts to a stock item record - for example putting parts back into stock. The in-stock quantity for each selected item is increased by the given amount.

{% with id="stock_add", url="stock/stock_add.png", description="Stock addition" %}
{% include 'img.html' %}
{% endwith %}

### Remove Stock

Remove parts from a stock item record - for example taking parts from stock for use. The in-stock quantity for each selected item is decreased by the given amount.

{% with id="stock_remove", url="stock/stock_remove.png", description="Stock removal" %}
{% include 'img.html' %}
{% endwith %}

### Count Stock

Count stock items (stocktake) to record the number of items in stock at a given point of time. The quantity for each part is pre-filled with the current quantity based on stock item history.

{% with id="stock_count", url="stock/stock_count.png", description="Stock count" %}
{% include 'img.html' %}
{% endwith %}
