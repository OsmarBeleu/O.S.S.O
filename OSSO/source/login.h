#pragma once
#include <wx/dnd.h>

class FileEvent : public wxFileDropTarget { // For general use; may be moved later. To handle events for dropping files, create one of this
private:

    void (*eventHandler)(wxCoord, wxCoord, const wxArrayString&);
    bool OnDropFiles(wxCoord x, wxCoord y, const wxArrayString& filenames) override;


public:

    FileEvent(void (*eventHandlerFunction)(wxCoord, wxCoord, const wxArrayString&)) : eventHandler(eventHandlerFunction){};
};



class LoginControl {
private:

static char (*key)[514];


public:

static int AttemptLogin(wxString password);
static void InputFile(wxString path);
static void PromptFile();

};