from medical_data_visualizer import draw_cat_plot, draw_heat_map

print("Generating catplot...")
fig1 = draw_cat_plot()
print("  Saved -> catplot.png")

print("Generating heatmap...")
fig2 = draw_heat_map()
print("  Saved -> heatmap.png")

print("Done.")
