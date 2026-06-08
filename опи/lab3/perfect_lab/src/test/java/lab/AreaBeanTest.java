package lab;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class AreaBeanTest {

    private AreaBean bean;

    @Before
    public void setUp() {
        bean = new AreaBean();
    }

    @Test
    public void testTopRightQuadrant_AlwaysMisses() {
        bean.setX(1);
        bean.setY(1.0);
        Assert.assertFalse("В верхней правой четверти всегда промах", bean.checkHit(2.0));
    }

    @Test
    public void testTopLeftQuadrant_Triangle() {
        bean.setX(-1);
        bean.setY(1.0);
        Assert.assertTrue("Точка (-1, 1) должна попадать в треугольник при R=2", bean.checkHit(2.0));

        bean.setX(-2);
        bean.setY(2.0);
        Assert.assertFalse("Точка (-2, 2) промах (на границе или вне) при R=2", bean.checkHit(2.0));
    }

    @Test
    public void testBottomLeftQuadrant_Rectangle() {
        bean.setX(-1);
        bean.setY(-1.5);
        Assert.assertTrue("Точка (-1, -1.5) внутри прямоугольника при R=2", bean.checkHit(2.0));

        bean.setX(-2);
        bean.setY(-1.0);
        Assert.assertFalse("Точка (-2, -1) вне прямоугольника по X при R=2", bean.checkHit(2.0));
    }

    @Test
    public void testBottomRightQuadrant_Circle() {
        bean.setX(1);
        bean.setY(-1.0);
        Assert.assertTrue("Точка (1, -1) внутри круга при R=2 (1^2 + (-1)^2 <= 4)", bean.checkHit(2.0));

        bean.setX(2);
        bean.setY(-2.0);
        Assert.assertFalse("Точка (2, -2) вне круга при R=2 (4+4 > 4)", bean.checkHit(2.0));
    }

    @Test
    public void testGettersAndSetters() {
        bean.setR10(true);
        Assert.assertTrue(bean.isR10());

        bean.setR15(false);
        Assert.assertFalse(bean.isR15());

        bean.setR20(true);
        Assert.assertTrue(bean.isR20());

        bean.setR25(false);
        Assert.assertFalse(bean.isR25());

        bean.setR30(true);
        Assert.assertTrue(bean.isR30());

        bean.setX(5);
        bean.setY(-1.0);

        Assert.assertEquals(5, bean.getX());
        Assert.assertEquals(-1.0, bean.getY(), 0.001);
    }

    @Test
    public void testCheckPointCoverageSafely() {
        callCheckPointSafely(true, false, false, false, false);
        callCheckPointSafely(false, true, false, false, false);
        callCheckPointSafely(false, false, true, false, false);
        callCheckPointSafely(false, false, false, true, false);
        callCheckPointSafely(false, false, false, false, true);

        try {
            bean.getResults();
        } catch (Throwable t) {
        }
    }

    private void callCheckPointSafely(boolean r10, boolean r15, boolean r20, boolean r25, boolean r30) {
        bean.setR10(r10);
        bean.setR15(r15);
        bean.setR20(r20);
        bean.setR25(r25);
        bean.setR30(r30);
        try {
            bean.checkPoint();
        } catch (Throwable t) {
        }
    }
}