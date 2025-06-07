from datetime import date, timedelta

class Plant:
    def __init__(self, name, sort, watering_freq, fertilizer_freq,
                 last_watering, last_fertilizer, last_transplant,
                 image='', description=''):
        self.name = name
        self.sort = sort
        self.watering_freq = watering_freq
        self.fertilizer_freq = fertilizer_freq
        self.last_watering = last_watering
        self.last_fertilizer = last_fertilizer
        self.last_transplant = last_transplant
        self.image = image
        self.description = description

    @property
    def next_watering(self):
        return self.last_watering + timedelta(days=self.watering_freq)

    @property
    def next_fertilizer(self):
        return self.last_fertilizer + timedelta(days=self.fertilizer_freq)

    def to_dict(self):
        return {
            "name": self.name,
            "sort": self.sort,
            "watering_freq": self.watering_freq,
            "fertilizer_freq": self.fertilizer_freq,
            "last_watering": self.last_watering.strftime("%Y-%m-%d"),
            "last_fertilizer": self.last_fertilizer.strftime("%Y-%m-%d"),
            "last_transplant": self.last_transplant.strftime("%Y-%m-%d"),
            "image": self.image,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            sort=data["sort"],
            watering_freq=int(data["watering_freq"]),
            fertilizer_freq=int(data["fertilizer_freq"]),
            last_watering=date.fromisoformat(data["last_watering"]),
            last_fertilizer=date.fromisoformat(data["last_fertilizer"]),
            last_transplant=date.fromisoformat(data["last_transplant"]),
            image=data.get("image", ""),
            description=data.get("description", "")
        )
