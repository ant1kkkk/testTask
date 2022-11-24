from pydantic import BaseModel, Field, validator


class OpenStreetMap(BaseModel):
    place_id: int
    osm_type: str
    osm_id: int
    boundingbox: list
    lat: str
    lon: str
    display_name: str
