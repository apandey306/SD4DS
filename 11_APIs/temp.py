# TODO: Validate the input data to this function using Pydantic.
# This validates that the value for timestamps is a list of integers
# and the value for data is a list of floats. 
class TrendlineInput(BaseModel):
    timestamps: List[int]
    data: List[float]


# This function will accept data in JSON format as its input. 
# You can also improve your API documentation very easily by adding 
# a summary and description to the @app decorator arguments.
@app.post(
    "/fit_trendline/",
    summary="Fit a trendline to any data",
    description="Provide a list of integer timestamps and a list of floats",
)
def calculate_trendline(trendline_input: TrendlineInput):
    slope, r_squared = fit_trendline(trendline_input.timestamps, trendline_input.data)
    return {"slope": slope, "r_squared": r_squared}


@app.get("/country_trendline/{country}")
def calculate_country_trendline(country: str):
    slope, r_squared = country_trendline(country)
    return {"slope": slope, "r_squared": r_squared}