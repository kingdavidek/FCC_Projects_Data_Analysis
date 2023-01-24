def draw_plot():
    df = pd.read_csv(
    "epa-sea-level.csv")

    # Create scatter plot
    graph = df.plot(kind="scatter", x="Year", y="CSIRO Adjusted Sea Level", figsize=(6,6))

    # Create first line of best fit
    lingress1880 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_fit = np.linspace(np.min(df["Year"]), 2050, num=171, retstep=True)    #Get the x values for the line of best fit (which are just the year)
    x_fit = x_fit[0]        # linspace returns a tuple with the array we want as the first entry 
    y_fit = (x_fit*lingress1880[0]) + lingress1880[1]    #use y = mx+c to plot line of best fit. We query lingress1880 for the slope and y intercept
    graph.plot(x_fit, y_fit, "r-")


    # Create second line of best fit
    lingress2000 = linregress(df["Year"][119:], df["CSIRO Adjusted Sea Level"][119:])
    new_xdata = df["Year"][119:]
    x_fit2000 = np.linspace(np.min(new_xdata), 2050, num = 51, retstep = True)
    x_fit2000 = x_fit2000[0]
    y_fit2000 = (x_fit2000*lingress2000[0]) + lingress2000[1]
    graph.plot(x_fit2000, y_fit2000, "g-")


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()
