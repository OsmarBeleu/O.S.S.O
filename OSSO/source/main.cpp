#include <wx/wx.h>
#include <wx/msgdlg.h>
#include <wx/textctrl.h>
#include <wx/image.h>
#include <wx/event.h>
#include <wx/xrc/xmlres.h>

#include "../resources/icon.xpm"

#include "main.h"
#include "login.h"

// the application icon (under Windows it is in resources and even
// though we could still include the XPM here it would be unused)

// --------------------------------------------- Definitions ---------------------------------------------

#ifndef wxHAS_IMAGES_IN_RESOURCES
#endif


wxFrame* ProgramControl::currentWindow = nullptr; // Initializing this before it's too late

wxIMPLEMENT_APP(ProgramControl); // Creates application object (don't make it static)



bool ProgramControl::OnInit() {

  // --------------------------------------------- Initialize stuff ---------------------------------------------

  if (!wxApp::OnInit())
    return false; // Indentation markers are being quirky, oOOo!
  
  wxXmlResource::Get()->InitAllHandlers(); // Load XRC files; listed one by one just to be ~verbose~ explicit
  wxInitAllImageHandlers();
  wxXmlResource::Get()->Load("resources/resources.xrc");
  


  wxFrame* login;
  if (!(login = wxXmlResource::Get()->LoadFrame(nullptr, "LoginWindow"))) // Load, display and store login screen
    return false;

  login->Show(true);

  currentWindow = login;



  // --------------------------------------------- Setup file events ---------------------------------------------

  login->SetDropTarget(new FileEvent([](wxCoord x, wxCoord y, const wxArrayString& filenames){LoginControl::InputFile(filenames.Last());})); // Lambdas are beautiful, right? (If you said yes, you are more psychopathic than me)
  // Uhh, just ignore this line. It's basically creating a FileEvent object as a way to bind the file drop event to LoginControl::InputFile. I hope it has no memory leaks.

  wxWindow* fileInputButton = login->FindWindow("FileInput");
  fileInputButton->Bind(wxEVT_BUTTON, [](wxCommandEvent& event){LoginControl::PromptFile();});
  // Well, this one links LoginControl::PromptFile to clicking the file button



  return true;
}
