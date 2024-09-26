ass MyCalendar:

        def __init__(self):
            self.timeSlots = []

                                  def book(self, start: int, end: int) -> bool:
            if self.confirmBooking(start, end):
                    self.timeSlots.append([start, end])
                    return True
        return False

    def confirmBooking(self, start, end):
            for x,y in self.timeSlots:
                    if (start >= x and start < y) or (end > x and end <= y):
                            return False
            if x > start and y < end:
                        return False
        return True
# Your MyCalendar object will be instantiated and called as such:
# # obj = MyCalendar()
# # param_1 = obj.book(start,end)
