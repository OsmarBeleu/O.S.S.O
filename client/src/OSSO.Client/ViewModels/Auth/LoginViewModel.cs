using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;

namespace OSSO.Client.ViewModels.Auth;

public partial class LoginViewModel : ObservableObject
{
    [ObservableProperty]
    private string _username = string.Empty;

    [ObservableProperty]
    private string _password = string.Empty;

    [ObservableProperty]
    private string _errorMessage = string.Empty;

    [ObservableProperty]
    private bool _isLoading = false;

    [RelayCommand]
    private void Login()
    {
        if (string.IsNullOrWhiteSpace(Username) ||
            string.IsNullOrWhiteSpace(Password))
        {
            ErrorMessage = "Preencha usuario e senha.";
            return;
        }

        ErrorMessage = string.Empty;
        IsLoading = true;
    }
}