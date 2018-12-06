from pytest_factoryboy import register
from crm import factories
import pytest

from home.factories import SiteFactory, HomePageFactory

register(factories.CityFactory)
register(factories.EmployeeFactory)
register(factories.ChannelFactory)
register(factories.RecruiterFactory)
register(factories.ProjectFactory)
register(factories.ClientCompanyFactory)
register(factories.MailboxFactory)
register(factories.MessageFactory)
register(factories.ProjectMessageFactory)
register(factories.UserFactory)
register(factories.AdminFactory, "admin_user")
register(SiteFactory)
register(HomePageFactory)


@pytest.fixture
def admin_app(django_app, admin_user):
    django_app.set_user(admin_user)
    return django_app


@pytest.fixture
def default_site(site_factory):
    return site_factory.create(is_default_site=True)
