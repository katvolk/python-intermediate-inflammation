"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
Authors: Kat Volk, Daniel Egbo, Markus Hundertmark, and Alessandro Mazzi
"""

import numpy as np

class Observation:
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self,other):
        return self.day == other.day and self.value == other.value


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Patient(Person):
    """A patient in an inflammation study."""
    def __init__(self, name, observations=None):
        super().__init__(name)

        self.observations = []
        if observations is not None:
            self.observations = observations

    def add_observation(self, value, day=None):
        """Add an observation to the patient.
        
        :param value: inflammation value for the day
        :param day: day of the observation, optional
        :returns: Observation instance with given value and day."""
        if day is None:
            try:
                day = self.observations[-1].day + 1
            except IndexError:
                day = 0
        new_observation = Observation(value, day)
        self.observations.append(new_observation)
        return new_observation

    def __eq__(self,other):
        return (self.name == other.name and
                self.observations == other.observations)


class Doctor(Person):
    """A doctor in an inflammation study with patients"""
    def __init__(self, name):
        super().__init__(name)
        self.patients = []

    def add_patient(self, new_patient):
        for patient in self.patients:
            if patient.name == new_patient.name:
                return
        self.patients.append(new_patient)


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.
    :param data: 2D data array (each row contains measurements for a single patient across all days)
    :returns: array of average values (one per row in data)
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2d inflammation data array.
    :param data: 2D data array (each row contains measurements for a single patient across all days)
    :returns: array of maximum values (one per row in data)
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2d inflammation data array.
    :param data: 2D data array (each row contains measurements for a single patient across all days)
    :returns: array of minimum values (one per row in data)
    """
    return np.min(data, axis=0)


def patient_normalise(data):
    """
    Normalise patient data between 0 and 1 of a 2D inflammation data array.

    Any NaN values are ignored, and normalised to 0

    :param data: 2D data array (each row contains measurements for a single patient across all days)
    :raises ValueError: raised if any entries in data are <0
    :returns: array of minimum values (one per row in data)
    """
    if not isinstance(data, np.ndarray):
        raise TypeError('data input should be ndarray')
    if len(data.shape) != 2:
        raise ValueError('inflammation array should be 2-dimensional')
    if np.any(data < 0):
        raise ValueError('Inflammation values should not be negative')
    max_data = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max_data[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised
