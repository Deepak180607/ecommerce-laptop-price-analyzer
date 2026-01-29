import scraper as sc
import analysis as an
import visualize as vs
sc.scrape_data()
an.clean_data()
vs.make_plots()
print(an.clean_data())