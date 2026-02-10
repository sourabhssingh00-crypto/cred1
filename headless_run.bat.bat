pytest -v -s -n=auto --html=Html_reports\myheadless_report_31st_jan_2026.html --browser headless -k "tittle"
pytest -n=auto --html=Html_reports\my_Chrome_report_31st_jan_2026.html --browser chrome -k "tittle"
pytest -n=auto --html=Html_reports\my_firefox_report_31st_jan_2026.html --browser firefox -k "tittle"
pytest -n=auto --html=Html_reports\my_Edge_report_31st_jan_2026.html --browser edge -k "tittle"