package lab;

import org.junit.Assert;
import org.junit.Test;

public class ResultTest {

    @Test
    public void testResultCreationAndGettersSetters() {
        Result result = new Result(1, 5, 2.5, 3.0, true);

        Assert.assertEquals(1, result.getId());
        Assert.assertEquals(5, result.getX());
        Assert.assertEquals(2.5, result.getY(), 0.001);
        Assert.assertEquals(3.0, result.getR(), 0.001);
        Assert.assertTrue(result.isHit());

        result.setId(2);
        result.setX(-3);
        result.setY(-1.5);
        result.setR(1.0);
        result.setHit(false);

        Assert.assertEquals(2, result.getId());
        Assert.assertEquals(-3, result.getX());
        Assert.assertEquals(-1.5, result.getY(), 0.001);
        Assert.assertEquals(1.0, result.getR(), 0.001);
        Assert.assertFalse(result.isHit());
    }
}