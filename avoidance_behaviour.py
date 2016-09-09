#!/usr/bin/env python

import boatdclient

from navigate import Navigator

# Point 0 must be on the left, point 1 on the right
# when looking upwind
points = boatdclient.get_current_waypoints()
avoid_points = []

class VisualObstacleAvoidance(Navigator):
    def __init__(self, namespace):
        super(TestBehaviour, self).__init__()
        self.set_target(points[0])
        self.current_point = 0
        self.avoid_current_point = 0
        self.distance_down = 20
        self.distance_across = 20
        self.BOX_BOTTOM_DIRECTION = points[0].bearing_to(points[1]) + Bearing(90)
        self.avoiding = False

        self.waypoint_checkoff_distance = 8

        # shared messaging between processes
        self.namespace = namespace

    def check_new_target(self):
        if self.namespace.is_obstacle_detected is True and self.avoiding is False:
            self.avoiding = True
           # avoid_points.append(self.current_point.relative_point(BOX_BOTTOM_DIRECTION, self.distance_down))
            if self.current_point == 0
                avoid_points.append(self.current_point.relative_point(BOX_BOTTOM_DIRECTION + Bearing(25), self.distance_down))
                avoid_points.append(points[0].relative_point(self.current_point.bearing_to(points[0]), self.distance_across))                
            if self.current_point == 1
                avoid_points.append(self.current_point.relative_point(BOX_BOTTOM_DIRECTION - Bearing(25), self.distance_down))
                avoid_points.append(points[1].relative_point(self.current_point.bearing_to(points[1]), self.distance_across))
            self.set_target(avoid_points[0])
            
        elif self.avoiding is True:
            if self.avoid_current_point > len(avoid_points) - 1:
                self.avoiding = False 
            else:
                distance = self.boat.position.distance_to(self.target)
                if distance <= self.waypoint_checkoff_distance:
                    print 'distance from point:', distance
                    self.avoid_current_point += 1
                    return avoid_points[self.avoid_current_point]
                else:
                    print 'distance to point', distance
                    return None
                
        
        if self.avoiding is False:
            if self.current_point > len(points) - 1:
                self.current_point = 0 
                return points[self.current_point]
            else:
                distance = self.boat.position.distance_to(self.target)
                if distance <= self.waypoint_checkoff_distance:
                    print 'distance from point:', distance
                    self.current_point += 1
                    return points[self.current_point]
                else:
                    print 'distance to point', distance
                    return None

if __name__ == '__main__':
    behaviour = VisualObstacleAvoidance()
    behaviour.run()
