from database import Database

class main:
  def __init__(self):
    self.db=Database()
    self.db.create_table()
    self.current_note_id = None

  
#creation
  def create_new_note(self):
    self.current_note_id = None
    return True

  def save_note(self,title,content):
    title_clean = title.strip() if title else ""
    content_clean = content.strip() if content else ""

    
#validation
     if not title_clean and not content_clean:
       return False,"Cannot save an empty note."

     if not title_clean:
       title_clean = "Untitled Note"

#edit
      if self.current_note_id is not None:
        success=self.db.EDIT_note (self.current_note_id,title_clean,content_clean)
        if success:
          return True,"Note Updated successfully!"
        returnFalse,"Failed to update Note."

#creation
     else:    
       new_id=self.db.create_note(title_clean,content_clean)
       if new_id:
         self.current_note_id=new_id
         return True,"Note created successfully!"
        return False,"Failed to create note."


#view
    def load_note(self, note_id):
      note = self.db.view_note(note_id)
        if note:
            self.current_note_id = note_id  
            return note
        return None


  #
  def get_sidebar_list(self):
        notes = self.db.slidebar_note()
        return notes if notes is not None else []


# deletio
  def delete_current_note(self):
      if self.current_note_id is None:
          return False, "No note selected to delete."

      success = self.db.delete_note(self.current_note_id)
      if success:
          self.current_note_id = None  
          return True, "Note deleted successfully!"
       return False, "Failed to delete note."
    
