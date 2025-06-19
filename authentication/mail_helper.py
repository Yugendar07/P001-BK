def send_registration_email(first_name, last_name, title, ):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    html_message =f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 0;">
    <div style="background-color: #f0f0f0; padding: 20px;">
        <table style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border-collapse: collapse;">
            <tr>
                <td style="padding: 20px;">
                    <h1 style="color: #333333;">{title}</h1>
                    <p style="color: #666666;">Hi {first_name} {last_name},</p>
                    <p style="color: #666666;">Your {title} OTP for Bingo Jobs is <strong></strong>. OTP will expire in the next 2 minutes.</p>
                    <p style="color: #666666;">Best regards,<br><b>Team</b><br>Bingo Jobs</p>
                    <p style="color: #666666; font-weight: bold;"></p>
                </td>
            </tr>
        </table>
    </div>
</body>
</html>"""

