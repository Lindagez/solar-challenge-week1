# Apply final filter
if selected_countries:
    filt_df = filt_df[filt_df["country"].astype(str).isin(selected_countries)]

# ----------------------------
# Layout
# ----------------------------
left, right = st.columns([2, 1])

with left:
    st.subheader("Distribution by Country")
    if plot_type == "Boxplot":
        fig = px.box(
            filt_df, x="country", y=metric, points="all", color="region",
            title=f"{metric} distribution by country",
        )
    elif plot_type == "Violin":
        fig = px.violin(
            filt_df, x="country", y=metric, box=True, points="all", color="region",
            title=f"{metric} distribution by country",
        )
    elif plot_type == "Histogram":
        fig = px.histogram(
            filt_df, x=metric, color="region", barmode="overlay", nbins=30,
            title=f"{metric} histogram",
        )
    else:  # Bar (mean by country)
        means = (
            filt_df.groupby(["country", "region"], as_index=False)[metric]
            .mean()
            .sort_values(metric, ascending=False)
        )
        fig = px.bar(
            means, x="country", y=metric, color="region", title=f"Mean {metric} by country"
        )
    fig.update_layout(xaxis_title="Country", yaxis_title=metric, legend_title="Region")
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Top Regions (by mean)")
    region_stats = (
        filt_df.groupby("region", as_index=False)[metric]
        .agg(["count", "mean", "median", "std"])  # type: ignore
        .reset_index()
        .rename(columns={"mean": f"mean_{metric}", "median": f"median_{metric}", "std": f"std_{metric}"})
        .sort_values(f"mean_{metric}", ascending=False)
    )
    st.dataframe(region_stats, use_container_width=True)

    st.markdown("---")
    st.subheader("Download filtered data")
    st.download_button(
        label="Download CSV",
        data=filt_df.to_csv(index=False).encode("utf-8"),
        file_name=f"filtered_{metric.lower()}.csv",
        mime="text/csv",
    )

# Footer notes
st.markdown(
    """
    ---
    Notes
    - Place your dataset(s) under ./data (this folder is ignored by git).
    - Required columns: country, region. Include GHI or any numeric metric to plot.
    - Use the sidebar to switch datasets and plot types; all charts are interactive.
    """
)
