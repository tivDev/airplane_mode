Thanks, Tiv! Here's the corrected `README.md` with the proper `bench get-app` command:

---

````markdown
# Airplane Mode ✈️

**Airplane Mode** is a custom app built on the [Frappe Framework](https://frappeframework.com), designed to manage flights, airplanes, tickets, passengers, and other airline-related data.

---

## Features

- Manage Airlines, Airplanes, and Flights
- Create and issue Airplane Tickets
- Track Passengers with custom naming rules
- Web views for flight listings and ticket details
- Extendable to include crew members, gate assignments, and airport shops

---

## Requirements

- [Frappe Framework](https://frappeframework.com) v14 or later
- Python 3.10+
- Node.js 16+
- Redis Server
- MariaDB 10.6+
- Yarn

---

## Installation

### 1. Set Up Frappe Bench

If you haven't already:

```bash
# Install Bench CLI
pip install frappe-bench

# Create a new bench
bench init frappe-bench --frappe-branch version-14
cd frappe-bench
````

### 2. Get the App

Use the `bench get-app` command:

```bash
bench get-app https://github.com/tivDev/airplane_mode.git
```

### 3. Create a New Site

```bash
bench new-site airplane.local
```

Follow the prompts to set up the database and admin credentials.

### 4. Install the App on the Site

```bash
bench --site airplane.local install-app airplane_mode
```

### 5. Start the Server

```bash
bench start
```

Then visit [http://localhost:8000](http://localhost:8000) in your browser.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Repository

GitHub: [https://github.com/tivDev/airplane\_mode](https://github.com/tivDev/airplane_mode)

---

## Contributing

Pull requests are welcome! If you want to propose major changes, please open an issue first to discuss.

---

## Maintainer

Maintained by [Tiv Nguot](https://github.com/tivDev)

```

---

Let me know if you'd like to include example screenshots, GIFs, or docs links!
```
