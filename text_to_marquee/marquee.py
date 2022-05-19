import json
import tempfile
from typing import Optional, Tuple
import os
from PIL import Image, ImageDraw, ImageFont
from pydantic import BaseModel, validator

PATH = os.path.dirname(os.path.abspath(__file__))


class Text(BaseModel):
    text: str
    color: Tuple[int, int, int]
    box_square_width: int
    font: Optional[str] = None
    left_top_location: Tuple[int, int]

    @validator("color", "left_top_location", pre=True)
    def validate_tuple(cls, field_value):
        return tuple(field_value)

    @validator("font", always=True)
    def read_font(cls, value, values):
        return ImageFont.truetype(value, values["box_square_width"], encoding="utf-8")


class Background(BaseModel):
    width: int
    height: int
    color: Tuple[int, int, int]

    @validator("color", pre=True)
    def validate_tuple(cls, field_value):
        return tuple(field_value)


class Config(BaseModel):
    text: Text
    background: Background


class MarqueeGenerator:
    def __init__(self, text: str, config_path: str) -> None:
        self.config_path = config_path if config_path else f"{PATH}/static/configs.json"
        with open(self.config_path) as filep:
            data = json.load(filep)
        if text:
            data["text"]["text"] = text
        self.config = Config(**data)
        self.imagelist = []

    def generate_pictures(self, tmpdir: str):
        frame = Image.new(
            "RGB",
            (
                self.config.background.width,
                self.config.background.height,
            ),
            color=self.config.background.color,
        )
        draw = ImageDraw.Draw(frame)
        draw.text(
            xy=self.config.text.left_top_location,
            text=self.config.text.text,
            fill=self.config.text.color,
            font=self.config.text.font,
        )
        box = [
            0,
            0,
            self.config.text.box_square_width,
            self.config.text.box_square_width,
        ]
        interval = 0.1 * self.config.text.box_square_width
        for i in range(int(self.config.background.width / interval)):
            if (
                self.config.text.box_square_width + interval * i
                < self.config.background.width
            ):
                box = [
                    0 + interval * i,
                    0,
                    self.config.text.box_square_width + 10 * i,
                    self.config.text.box_square_width,
                ]
                region = frame.crop(box)
                filename = f"{tmpdir}/{str(i)}.png"
                region.save(filename)
                self.imagelist.append(Image.open(filename))

    def concat_pictures(self):
        self.imagelist[0].save(
            "out.gif",
            format="GIF",
            save_all=True,
            append_images=self.imagelist[1:],
            duration=40,
            optimize=True,
            loop=0,
        )

    def run(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            self.generate_pictures(tmpdir=tmpdir)
            self.concat_pictures()


def text_to_marquee(text: str, config_path: str) -> None:
    generator = MarqueeGenerator(text=text, config_path=config_path)
    generator.run()
