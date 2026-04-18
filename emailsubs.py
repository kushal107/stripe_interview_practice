"""Design a subscription management system that tracks user subscriptions and sends automated emails at specific lifecycle events."""

from enum import Enum
from datetime import datetime, timedelta
import uuid

# ------------------ Models ------------------

class SubscriptionStatus(Enum):
    TRIALING = "trialing"
    ACTIVE = "active"
    CANCELED = "canceled"

class Subscription:
    def __init__(self, user_id, plan, trial_days=7):
        self.user_id = user_id
        self.plan = plan
        self.status = SubscriptionStatus.TRIALING
        self.trial_end = datetime.now() + timedelta(days=trial_days)


# ------------------ Event Bus ------------------

class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, handler):
        self.subscribers.setdefault(event_type, []).append(handler)

    def publish(self, event_type, event):
        for handler in self.subscribers.get(event_type, []):
            handler(event)


# ------------------ Notification Service ------------------

class NotificationService:
    def __init__(self):
        self.processed_events = set()  # idempotency

    def handle_event(self, event):
        event_id = event["id"]

        if event_id in self.processed_events:
            return  # avoid duplicate email

        print(f"[EMAIL] {event['type']} -> user {event['user_id']}")
        self.processed_events.add(event_id)


# ------------------ Subscription Service ------------------

class SubscriptionService:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.subscriptions = {}

    def create_subscription(self, user_id, plan):
        sub = Subscription(user_id, plan)
        self.subscriptions[user_id] = sub

        self._emit("subscription.created", user_id)
        return sub

    def cancel_subscription(self, user_id):
        sub = self.subscriptions.get(user_id)
        if not sub:
            return

        sub.status = SubscriptionStatus.CANCELED
        self._emit("subscription.canceled", user_id)

    def check_trial_expiry(self):
        for sub in self.subscriptions.values():
            if (
                sub.status == SubscriptionStatus.TRIALING
                and sub.trial_end <= datetime.now()
            ):
                sub.status = SubscriptionStatus.ACTIVE
                self._emit("subscription.trial_ended", sub.user_id)

    def _emit(self, event_type, user_id):
        event = {
            "id": str(uuid.uuid4()),
            "type": event_type,
            "user_id": user_id,
        }
        self.event_bus.publish(event_type, event)

#-----------------Test cases-----------------------
def test_create_subscription():
    event_bus = EventBus()
    service = SubscriptionService(event_bus)

    sub = service.create_subscription("user_1", "pro")

    assert sub.user_id == "user_1"
    assert sub.status == SubscriptionStatus.TRIALING


def test_cancel_subscription():
    event_bus = EventBus()
    service = SubscriptionService(event_bus)

    service.create_subscription("user_1", "pro")
    service.cancel_subscription("user_1")

    assert service.subscriptions["user_1"].status == SubscriptionStatus.CANCELED


# ------------------ Wiring ------------------

event_bus = EventBus()
notification_service = NotificationService()

event_bus.subscribe("subscription.created", notification_service.handle_event)
event_bus.subscribe("subscription.canceled", notification_service.handle_event)
event_bus.subscribe("subscription.trial_ended", notification_service.handle_event)

service = SubscriptionService(event_bus)

# Demo
service.create_subscription("user_1", "pro")
service.cancel_subscription("user_1")
service.check_trial_expiry()

#test cases
test_create_subscription()
test_cancel_subscription()
print("All tests passed!")