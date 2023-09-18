<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the number of rakes from the form
    $numRakes = $_POST["numRakes"];

    // Define the email content
    $subject = "Request for Railway Rakes for Coal Transportation";
    $message = "
        [Your Name]
        [Your Address]
        [City, State, PIN Code]
        [Your Email Address]
        [Your Contact Number]
        [Date]

        [Recipient's Name]
        [Recipient's Designation]
        [Ministry/Department Name]
        [Government of India]
        [Address]
        [City, State, PIN Code]

        Subject: $subject

        Dear [Recipient's Name],

        I hope this letter finds you in good health and high spirits. I am writing to request the allocation of railway rakes for coal transportation as an essential requirement for our ongoing operations and the greater benefit of the nation's economy.

        [Provide some context about your organization, such as its name, type of coal-related activities, and any significant contributions to the sector.]

        As you are aware, coal is a vital resource that fuels various industries and power generation units across the country. The efficient and timely transportation of coal plays a crucial role in ensuring the uninterrupted supply of energy and raw materials to these sectors. Railway transportation has been one of the most reliable and cost-effective means of coal distribution in India.

        However, our organization is currently facing challenges due to an insufficient allocation of railway rakes for coal transportation. This shortage is hindering our ability to meet our commitments to our customers, affecting production schedules, and ultimately impacting the nation's industrial and energy sectors.

        We kindly request the Ministry/Department [mention the relevant ministry or department responsible for railway rakes allocation] to consider our plea for a more substantial allocation of railway rakes to facilitate the efficient and timely transport of coal. This allocation will not only benefit our organization but will also contribute to the overall growth of the coal sector and the nation's economy.

        We are fully committed to complying with all government regulations and ensuring the safe and responsible transportation of coal. We understand the importance of efficient resource allocation and pledge to utilize the allocated railway rakes judiciously and in alignment with the nation's interests.

        We are open to discussing the specific details of our requirements and how we can collaborate with the relevant authorities to streamline the coal transportation process further.

        I kindly request an opportunity for a meeting to discuss this matter in detail and explore potential solutions to address the current challenges. Your guidance and support in this regard would be highly appreciated.

        Thank you for your attention to this crucial matter. We look forward to a positive response and the opportunity to work together for the betterment of the coal industry and the nation.

        Sincerely,

        [Your Name]
        [Your Designation]
        [Name of Your Organization]

        Number of Rakes Needed: $numRakes
    ";

    // Define recipient's email address
    $to = "recipient@example.com"; // Replace with the actual recipient's email address

    // Additional email headers
    $headers = "From: your_email@example.com" . "\r\n" .
               "Reply-To: your_email@example.com" . "\r\n" .
               "X-Mailer: PHP/" . phpversion();

    // Send the email
    mail($to, $subject, $message, $headers);

    // Redirect to a thank you page or display a confirmation message
    header("Location: thank_you.html");
    exit;
}
?>
