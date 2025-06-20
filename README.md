# Vonage SMS Sender Application

## Overview

This application utilizes the Vonage API to send SMS messages to a list of recipients based on data from an XLS file. It simplifies the process of sending bulk SMS messages, making it ideal for notifications, alerts, or marketing campaigns.

## Features

- Read recipient data from an XLS file
- Send SMS messages to multiple recipients using the Vonage API
- Handle responses and errors for each SMS sent
- Easy configuration for API credentials

## Technologies Used

- Java
- Vonage API
- Apache POI (for reading XLS files)

## Getting Started

### Prerequisites

- Java 11 or higher
- Maven
- Vonage API account (for API key and secret)
- An XLS file containing recipient phone numbers and messages

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/vonage-sms-sender.git
   cd vonage-sms-sender
