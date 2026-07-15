#pragma once

#include <wx/wx.h>

class ProgramControl : public wxApp {
private:

    static wxFrame* currentWindow;


public:

    bool OnInit() override;
    wxFrame* GetCurrentWindow() {return currentWindow;};

};