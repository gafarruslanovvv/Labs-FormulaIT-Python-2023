from __future__ import annotations
from typing import Union


class MaterialObject:
    def __init__(self, mass: float, volume: float):
        """
        Initialize a material object with mass and volume.

        :param mass: Mass of the material object.
        :param volume: Volume of the material object.

        Example:
        >>> obj = MaterialObject(10.0, 5.0)
        """
        if not isinstance(mass, (int, float)):
            raise TypeError("Mass should be of type int or float.")
        if mass <= 0:
            raise ValueError("Mass should be a positive number.")
        self.mass: float = mass

        if not isinstance(volume, (int, float)):
            raise TypeError("Volume should be of type int or float.")
        if volume <= 0:
            raise ValueError("Volume should be a positive number.")
        self.volume: float = volume

    def calculate_density(self) -> float:
        """
        Calculate the density of the material object.

        :return: Density of the material object.

        Example:
        >>> obj = MaterialObject(10.0, 5.0)
        >>> obj.calculate_density()
        """
        ...

    def reshape_object(self, new_volume: float) -> None:
        """
        Change the volume of the material object.

        :param new_volume: New volume of the material object.

        :raise ValueError: If the new volume is not a positive number.

        Example:
        >>> obj = MaterialObject(10.0, 5.0)
        >>> obj.reshape_object(8.0)
        """
        ...


class TechnicalDevice:
    def __init__(self, brand: str, year_of_manufacture: int):
        """
        Initialize a technical device with brand and year of manufacture.

        :param brand: Brand or name of the technical device.
        :param year_of_manufacture: Year of manufacture of the technical device.

        Example:
        >>> device = TechnicalDevice("ABC", 2022)
        """
        if not isinstance(brand, str):
            raise TypeError("Brand should be of type str.")
        if not brand:
            raise ValueError("Brand should not be an empty string.")
        self.brand: str = brand

        if not isinstance(year_of_manufacture, int):
            raise TypeError("Year of manufacture should be of type int.")
        if year_of_manufacture < 0:
            raise ValueError("Year of manufacture should be a non-negative number.")
        self.year_of_manufacture: int = year_of_manufacture

    def turn_on(self) -> None:
        """
        Turn on the technical device.

        Example:
        >>> device = TechnicalDevice("ABC", 2022)
        >>> device.turn_on()
        """
        ...

    def turn_off(self) -> None:
        """
        Turn off the technical device.

        Example:
        >>> device = TechnicalDevice("ABC", 2022)
        >>> device.turn_off()
        """
        ...


class SocialNetwork:
    def __init__(self, name: str, user_count: int):
        """
        Initialize a social network with name and user count.

        :param name: Name of the social network.
        :param user_count: Number of registered users in the social network.

        Example:
        >>> network = SocialNetwork("MyNetwork", 1000000)
        """
        if not isinstance(name, str):
            raise TypeError("Name should be of type str.")
        if not name:
            raise ValueError("Name should not be an empty string.")
        self.name: str = name

        if not isinstance(user_count, int):
            raise TypeError("User count should be of type int.")
        if user_count < 0:
            raise ValueError("User count should be a non-negative number.")
        self.user_count: int = user_count

    def create_post(self, text: str) -> None:
        """
        Create a new post in the social network.

        :param text: Text content of the post.

        Example:
        >>> network = SocialNetwork("MyNetwork", 1000000)
        >>> network.create_post("Hello, world!")
        """
        ...

    def add_friend(self, friend: str) -> None:
        """
        Add a friend to the user's contacts in the social network.

        :param friend: Name or username of the friend to be added.

        Example:
        >>> network = SocialNetwork("MyNetwork", 1000000)
        >>> network.add_friend("JohnDoe")
        """
        ...
