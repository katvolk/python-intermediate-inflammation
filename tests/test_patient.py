"""Tests for the Patient model."""


def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)
    assert p.name == name


def test_create_doctor():
    from inflammation.models import Doctor

    name = 'Dr. Who'
    d = Doctor(name=name)
    assert d.name == name


def test_add_patient():
    """make sure adding patients works"""
    from inflammation.models import Doctor
    from inflammation.models import Patient

    d = Doctor(name='Dr. Who')
    p = Patient(name='Amy')
    d.add_patient(p)
    assert d.patients is not None
    assert len(d.patients) == 1

def test_doctor_is_person():
    """Check if a doctor is a person."""
    from inflammation.models import Doctor, Person
    doc = Doctor("Sheila Wheels")
    assert isinstance(doc, Person)


def test_patient_is_person():
    """Check if a patient is a person. """
    from inflammation.models import Patient, Person
    alice = Patient("Alice")
    assert isinstance(alice, Person)


def test_add_mulitple_patients():
    """add two patients, re-add first patient to make sure there
    aren't any duplicates
    """
    from inflammation.models import Doctor
    from inflammation.models import Patient

    d = Doctor(name='Dr. Who')
    p1 = Patient(name='Amy')
    d.add_patient(p1)
    p2 = Patient(name='Rory')
    d.add_patient(p2)
    p3 = Patient(name='Amy')
    d.add_patient(p3)
    assert d.patients is not None
    assert len(d.patients) == 2
    assert p3==p1


def test_compare_patients():
    """add two patients, re-add first patient to make sure there
    aren't any duplicates
    """
    from inflammation.models import Patient

    p1 = Patient(name='Amy')
    p1.add_observation([1,2,3,4,5])
    p2 = Patient(name='Amy')
    p2.add_observation([1,2,3,4,5])
    p3 = Patient(name='Amy')
    p3.add_observation([1,4,5])
    assert not p3 == p1
    assert p1 == p2