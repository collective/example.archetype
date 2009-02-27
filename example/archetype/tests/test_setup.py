from base import InstantMessageTestCase

class TestProductInstall(InstantMessageTestCase):

    def afterSetUp(self):
        self.types = ('InstantMessage',)

    def testTypesInstalled(self):
        for t in self.types:
            self.failUnless(t in self.portal.portal_types.objectIds(),
                            '%s content type not installed' % t)

    def testPortalFactoryEnabled(self):
        for t in self.types:
            self.failUnless(t in self.portal.portal_factory.getFactoryTypes().keys(),
                            '%s content type not installed' % t)

class TestInstantiation(InstantMessageTestCase):

    def testCreateInstantMessage(self):
        # Adding an InstantMessage anywhere - can only be done by a Manager or Portal Owner
        #self.setRoles(['Manager'])
        #self.loginAsPortalOwner()

        # Login as a manager and create
        # an item which is initially private page to play around with
        self.loginAsPortalOwner()
        self.portal.invokeFactory("Document", "doc")
        self.portal.invokeFactory('InstantMessage', 'im1')


        #self.portal.invokeFactory('InstantMessage', 'im1')
        #self.failUnless('im1' in self.portal.objectIds())
        #self.folder.invokeFactory('InstantMessage', 'im1')
        #self.failUnless('im1' in self.folder.objectIds())

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestProductInstall))
    suite.addTest(makeSuite(TestInstantiation))
    return suite
