#include "login.h"

#include <wx/window.h>
#include <wx/wx.h>
#include <wx/msgdlg.h>
#include <wx/filedlg.h>
#include <wx/wfstream.h>

bool FileEvent::OnDropFiles(wxCoord x, wxCoord y, const wxArrayString& filenames) {

    eventHandler(x, y, filenames);

    return true; // Who needs error checking? :sunglasses:
}



char buf[514] = {}; char (*LoginControl::key)[514] = &buf;


int LoginControl::AttemptLogin(wxString password){ // Decrypt and check .osso key with the password

    return 0; // Sucessful
};

void LoginControl::InputFile(wxString path){ // When file is input, process it and save to "key"
    
    if (path == "") // I don't know how the heck that would happen, but "it's not profound to know that you can never know"
    {
        wxMessageBox("Empty file path.", "Error");
        return;
    }

    wxFile file(path);
    if(!file.IsOpened())
    {
        wxMessageBox("Can't open file.", "Error");
        return;
    }

    if(file.Length() != 514)
    {
        wxMessageBox("Invalid .osso file.", "Error");
        return;
    }


    wxString text; // For debug; ought to remove later
    file.ReadAll(&text); // For debug; ought to remove later
    wxMessageBox(text);  // For debug; ought to remove later


    char blob[514]; // Uhhh, I guess I should note that there are 2 bytes for checking if decryption was successful and another 512 for the actual key
    file.Read(&blob, 514);
    key = &blob;

};

void LoginControl::PromptFile(){ // When key button is pressed, prompt for .osso file and process input
    
    wxFileDialog dialog(wxGetActiveWindow(), "Open private key file", ".", "", "OSSO key file (*.osso)|*.osso", wxFD_OPEN|wxFD_FILE_MUST_EXIST);

    if (dialog.ShowModal() == wxID_CANCEL)
        return;

    InputFile(dialog.GetPath()); // Centralization; yeah baby!
};