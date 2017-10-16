#!/bin/bash
d=$(date +%Y-%m-%d)
scrapy crawl dailymovie -o $d -t csv
mail -s "DailyMovie" magicyang876@outlook.com < $d
