content = '''<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:OSSO.Client.ViewModels.Auth"
             x:Class="OSSO.Client.Views.Auth.LoginView"
             x:DataType="vm:LoginViewModel">

    <Grid ColumnDefinitions="480,*">

        <!-- LADO ESQUERDO -->
        <Panel Grid.Column="0" Background="#0D0D0D">
            <Image Source="/Assets/Images/sidebar_bg.png"
                   Stretch="Fill"
                   HorizontalAlignment="Stretch"
                   VerticalAlignment="Stretch"/>
            <Image Source="/Assets/Images/sidebar_art.png"
                   Stretch="Uniform"
                   HorizontalAlignment="Center"
                   VerticalAlignment="Center"
                   Margin="20"/>
        </Panel>

        <!-- LADO DIREITO -->
        <Panel Grid.Column="1" Background="White">
            <StackPanel VerticalAlignment="Center"
                        HorizontalAlignment="Center"
                        Width="360"
                        Spacing="0">

                <TextBlock Text="O.S.S.O"
                           FontSize="42"
                           FontWeight="Bold"
                           Foreground="#0D0D0D"
                           HorizontalAlignment="Center"
                           Margin="0,0,0,6"/>

                <TextBlock Text="Faca login para continuar"
                           FontSize="14"
                           Foreground="#555555"
                           HorizontalAlignment="Center"
                           Margin="0,0,0,40"/>

                <!-- Campo usuario -->
                <Grid Height="72" Margin="0,0,0,8">
                    <Image Source="/Assets/Images/blob_field_1.png"
                           Stretch="Fill"/>
                    <TextBox Text="{Binding Username}"
                             PlaceholderText="Usuario"
                             Background="Transparent"
                             BorderThickness="0"
                             Foreground="#0D0D0D"
                             FontSize="16"
                             VerticalAlignment="Center"
                             HorizontalAlignment="Stretch"
                             Margin="32,0,32,0"/>
                </Grid>

                <!-- Campo senha -->
                <Grid Height="72" Margin="0,0,0,24">
                    <Image Source="/Assets/Images/blob_field_2.png"
                           Stretch="Fill"/>
                    <TextBox Text="{Binding Password}"
                             PlaceholderText="Senha"
                             PasswordChar="*"
                             Background="Transparent"
                             BorderThickness="0"
                             Foreground="#0D0D0D"
                             FontSize="16"
                             VerticalAlignment="Center"
                             HorizontalAlignment="Stretch"
                             Margin="32,0,32,0"/>
                </Grid>

                <!-- Erro -->
                <TextBlock Text="{Binding ErrorMessage}"
                           Foreground="#CC0000"
                           FontSize="12"
                           HorizontalAlignment="Center"
                           Margin="0,0,0,12"/>

                <!-- Botao -->
                <Grid Height="90">
                    <Image Source="/Assets/Images/blob_button.png"
                           Stretch="Fill"/>
                    <Button Content="Entrar"
                            Command="{Binding LoginCommand}"
                            Background="Transparent"
                            BorderThickness="0"
                            Foreground="White"
                            FontSize="18"
                            FontWeight="Bold"
                            HorizontalAlignment="Stretch"
                            HorizontalContentAlignment="Center"
                            VerticalAlignment="Center"/>
                </Grid>

            </StackPanel>
        </Panel>

    </Grid>

</UserControl>'''

with open('Views/Auth/LoginView.axaml', 'w', encoding='utf-8') as f:
    f.write(content)
print('LoginView.axaml atualizado!')