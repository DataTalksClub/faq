---
id: 5c68f358c2
question: Generate Evidently Chart in Grafana
section: Module 5: Monitoring
course: mlops-zoomcamp
sort_order: 2050
---

Problem: Can we generate charts like Evidently inside Grafana?

Solution: In Grafana that would be a stat panel (just a number) and scatter plot panel (I believe it requires a plug-in). However, there is no native way to quickly recreate this exact Evidently dashboard. You'd need to make sure you have all the relevant information logged to your Grafana data source, and then design your own plots in Grafana.

If you want to recreate the Evidently visualizations externally, you can export the Evidently output in JSON with include_render=True

(more details here ) and then parse information from it for your external visualization layer. To include everything you need for non-aggregated visuals, you should also add "raw_data": True  option (more details here ).

Overall, this specific plot with under- and over-performance segments is more useful during debugging, so might be easier to access it ad hoc using Evidently.

Added by Ming Jun, Asked by Luke, Answered by Elena Samuylova

