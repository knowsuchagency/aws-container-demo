from typing_extensions import TypedDict


class Weather(TypedDict):
    FeelsLikeC: str
    FeelsLikeF: str
    cloudcover: str
    humidity: str
    localObsDateTime: str
    observation_time: str
    precipInches: str
    precipMM: str
    pressure: str
    pressureInches: str
    temp_C: str
    temp_F: str
    uvIndex: str
    visibility: str
    visibilityMiles: str
    weatherCode: str
    weatherDesc: list[dict[str, str]]
    weatherIconUrl: list[dict[str, str]]
    winddir16Point: str
    winddirDegree: str
    windspeedKmph: str
    windspeedMiles: str
