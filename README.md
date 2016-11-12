# PyPlanner
CLI school assignment planner

## Usage
Open `plan.py` and `plan_server.py` and modify the IPs and ports to your preferences.

Run `plan_server.py` on your remote server. To run it in the background, use `nohup ./plan_server.py &`. 

On the client side, there are three modification commands for `plan.py`: `add`, `mod`, and `del`. 

To add, use `./plan.py add assignment class date`. Deletion is the same, but switch `add` with `del`. 

To modify, use `./plan.py mod old_assignment old_class old_date new_assignment new_class new_date`. As of now, dates must be in the format of mm/dd. 

To view your planner, run `./plan.py get`. Only assignments a week or less in advance will be displayed.
