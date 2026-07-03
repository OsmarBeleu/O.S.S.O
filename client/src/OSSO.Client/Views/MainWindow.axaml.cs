using Avalonia.Controls;
using OSSO.Client.ViewModels.Auth;

namespace OSSO.Client.Views;

public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();
        DataContext = new LoginViewModel();
    }
}