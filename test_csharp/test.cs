using System;
using System.Text;
using System.Globalization;

class Test
{
    static void Main()
    {
        Console.WriteLine("Ingrese una frase para verificar si es palindromo:");

        string? input = Console.ReadLine();

        try
        {
            bool result = IsPalindrome(input);
            Console.WriteLine(result);
        }
        catch (ArgumentException ex)
        {
            Console.WriteLine($"Error de entrada: {ex.Message}");
        }
    }

    public static string RemoveDiacritics(string text)
    {
        var normalized = text.Normalize(NormalizationForm.FormD);
        var sb = new StringBuilder(normalized.Length);

        foreach (char c in normalized)
        {
            var uc = CharUnicodeInfo.GetUnicodeCategory(c);
            if (uc != UnicodeCategory.NonSpacingMark)
                sb.Append(c);
        }

        return sb.ToString().Normalize(NormalizationForm.FormC);
    }

    public static bool IsPalindrome(string? text)
    {
        if (text == null)
            throw new ArgumentException("El texto no puede ser nulo.");

        text = RemoveDiacritics(text);

        var cleaned = new StringBuilder(text.Length);

        foreach (char c in text)
        {
            if (char.IsLetterOrDigit(c))
                cleaned.Append(char.ToLowerInvariant(c));
        }

        if (cleaned.Length == 0)
            throw new ArgumentException("El texto debe contener caracteres alfanumericos.");

        int left = 0;
        int right = cleaned.Length - 1;

        while (left < right)
        {
            if (cleaned[left] != cleaned[right])
                return false;

            left++;
            right--;
        }

        return true;
    }
}
