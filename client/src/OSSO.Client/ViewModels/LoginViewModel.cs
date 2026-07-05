using System.Threading.Tasks;
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using OSSO.Client.Services.Api;

namespace OSSO.Client.ViewModels;

public partial class LoginViewModel : ObservableObject
{
    private readonly AuthApiService _authService = new();

    [ObservableProperty]
    private string _username = string.Empty;

    [ObservableProperty]
    private string _password = string.Empty;

    [ObservableProperty]
    private string _errorMessage = string.Empty;

    [ObservableProperty]
    private bool _isLoading = false;

    [RelayCommand]
    private async Task Login()
    {
        if (string.IsNullOrWhiteSpace(Username) ||
            string.IsNullOrWhiteSpace(Password))
        {
            ErrorMessage = "Preencha usuário e senha.";
            return;
        }

        IsLoading = true;
        ErrorMessage = string.Empty;

        var result = await _authService.LoginAsync(Username, Password);

        IsLoading = false;

        if (result is null)
        {
            ErrorMessage = "Usuário ou senha incorretos.";
            return;
        }

        // login bem sucedido — por enquanto só mostra o token no console
        System.Console.WriteLine($"Login OK! Token: {result.AccessToken}");
    }
}