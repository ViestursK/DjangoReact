from django.test import TestCase

from .models import Note

class NoteModelTest(TestCase):
  def test_create_note(self):
    note = Note.objects.create(title="Test Note #1", content="This is the content of the Test note #1.")
    self.assertEqual(str(note), "Test Note #1")