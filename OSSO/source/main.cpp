#include <wx/wx.h>
#include <wx/image.h>
#include <wx/event.h>
#include <wx/xrc/xmlres.h>

#include "../resources/sample.xpm"

#include "main.h"

// the application icon (under Windows it is in resources and even
// though we could still include the XPM here it would be unused)
#ifndef wxHAS_IMAGES_IN_RESOURCES
#endif


wxFrame* ProgramControl::currentWindow = nullptr;

wxIMPLEMENT_APP(ProgramControl); // Creates application object (don't make it static)


// --------------------------------------------- Phew! That's a lot for definitions.

bool ProgramControl::OnInit() {
  
  if (!wxApp::OnInit())
    return false; // Indentation markers are being quirky, oOOo!
  
  wxXmlResource::Get()->InitAllHandlers(); // Load XRC files; listed one by one just to be ~verbose~ explicit
  wxInitAllImageHandlers();
  wxXmlResource::Get()->Load("resources/splashwindow.xrc");
  
  wxFrame* splash;
  if (!(splash = wxXmlResource::Get()->LoadFrame(nullptr, "SplashWindow"))) // Load, display and store splash screen
    return false;

  splash->Show(true);

  currentWindow = splash;





  return true;
}
