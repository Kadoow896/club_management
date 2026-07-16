# Tech Club Management System

A team project developed using **Odoo ERP** to simplify the management of a technical club through a centralized administrative dashboard.

## Overview

The system helps manage club operations in one place, including:

- Member Management
- Event Management
- Attendance Tracking
- Task Management

## Features

- Manage club members: technical track, contact info, join date, with archiving for former members.
- Create and organize events/workshops with a status flow (Draft → Confirmed → Done/Cancelled) and a calendar view.
- Record attendance per event with a one-click toggle.
- Assign and track tasks with due dates, priority, and a Kanban board grouped by status.
- Role-based access: separate **Manager** (full control) and **Member** (read/update) permission groups.
- Search filters and group-by views across members, events, attendance, and tasks.
- Centralized dashboard for club administration.

## Technologies Used

- Odoo 19
- Python
- XML (views)
- PostgreSQL
- Git & GitHub

## Team Members

| Name | Responsibility |
|------|----------------|
| Kadi | Task Management |
| Hala | Members Module |
| Layan | Events Module |
| Mayasim | Attendance Module |
| Jana | Integration & Testing |

## My Contribution

I developed the **Events Module** (workshop scheduling, status workflow, calendar view, attendee/task stat buttons), and extended the shared foundation across all four modules: added the Manager/Member permission groups, additional fields (contact info, due dates, priority), the Task Kanban board, and search/filter views.

## Future Improvements

- Email notifications
- Analytics dashboard
- Mobile-friendly interface
- Automated tests

## License

This project was developed for educational purposes.
