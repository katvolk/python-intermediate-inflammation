"""
Inflam module for serializing patients data
Authors: Kat Volk, Daniel Egbo, Markus Hundertmark, and Alessandro Mazzi
"""
"""Module containing serializers for patient and observation data."""
from inflammation import models
import json

class Serializer:
    """
    Base class that holds the design that’s shared with all other
    serializer classes
    """
    @classmethod
    def serialize(cls, instances):
        raise NotImplementedError

    @classmethod
    def save(cls, instances, path):
        raise NotImplementedError

    @classmethod
    def deserialize(cls, data):
        raise NotImplementedError

    @classmethod
    def load(cls, path):
        raise NotImplementedError


class ObservationSerializer(Serializer):
    """Serializer for observations"""
    model = models.Observation

    @classmethod
    def serialize(cls, instances):
        return [{
            'day': instance.day,
            'value': instance.value,
        } for instance in instances]

    @classmethod
    def deserialize(cls, data):
        return [cls.model(**d) for d in data]

class PatientSerializer(Serializer):
    """Serializer for Patients"""
    model = models.Patient

    @classmethod
    def serialize(cls, instances):
        return [{
            'name': instance.name,
            'observations': ObservationSerializer.serialize(instance.observations),
        } for instance in instances]

    @classmethod
    def deserialize(cls, data):
        instances = []

        for item in data:
            item['observations'] = ObservationSerializer.deserialize(item.pop('observations'))
            instances.append(cls.model(**item))

        return instances

    @classmethod
    def save(cls, instances, path):
        raise NotImplementedError

    @classmethod
    def load(cls, path):
        raise NotImplementedError


class PatientJSONSerializer(PatientSerializer):
    """Serializer for Patiens in JSON format"""
    @classmethod
    def save(cls, instances, path):
        with open(path, 'w') as jsonfile:
            json.dump(cls.serialize(instances), jsonfile)

    @classmethod
    def load(cls, path):
        with open(path) as jsonfile:
            data = json.load(jsonfile)

        return cls.deserialize(data)
