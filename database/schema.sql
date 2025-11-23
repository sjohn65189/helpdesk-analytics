-- schema.sql
-- SQLite schema for Helpdesk Analytics Project

-- Create table for incidents
CREATE TABLE IF NOT EXISTS incidents (
    IncidentID TEXT PRIMARY KEY,       -- Unique ID for each ticket
    UserID TEXT,                        -- User who submitted the ticket
    AgentID TEXT,                       -- Assigned agent/technician
    Category TEXT,                       -- Ticket category (Hardware, Software, etc.)
    Priority TEXT,                       -- Ticket priority (Critical, High, Medium, Low)
    Status TEXT,                         -- Ticket status (Resolved, Open, In Progress)
    DateCreated TEXT,                     -- Date ticket was created
    DateClosed TEXT,                      -- Date ticket was closed
    ResolutionTime_Hours REAL,            -- Total resolution time in hours
    SLA_Category TEXT,                    -- Derived SLA category: Fast/Moderate/Slow
    Overdue INTEGER                       -- Derived boolean flag: 1 if ResolutionTime_Hours > 48, else 0
);
