using System.Net.Http;
using System.Net.Http.Json;
using System.Threading.Tasks;

namespace OSSO.Client.Services.Api;

public class AuthApiService
{
    private readonly HttpClient _http;
    private const string BaseUrl = "http://127.0.0.1:8000/api/v1";

    public AuthApiService()
    {
        _http = new HttpClient();
    }

    public async Task<LoginResult?> LoginAsync(string username, string password)
    {
        var body = new { username, password };
        var response = await _http.PostAsJsonAsync($"{BaseUrl}/auth/login", body);

        if (!response.IsSuccessStatusCode)
            return null;

        return await response.Content.ReadFromJsonAsync<LoginResult>();
    }

    public async Task<bool> RegisterAsync(string username, string password, string publicKey)
    {
        var body = new { username, password, public_key = publicKey };
        var response = await _http.PostAsJsonAsync($"{BaseUrl}/auth/register", body);
        return response.IsSuccessStatusCode;
    }
}

public class LoginResult
{
    public string AccessToken { get; set; } = string.Empty;
    public string Username { get; set; } = string.Empty;
}